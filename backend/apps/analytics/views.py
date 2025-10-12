from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg, Sum, Q
from django.utils import timezone
from datetime import timedelta

from apps.students.models import Student
from apps.staff.models import Staff
from apps.attendance.models import Attendance
from apps.fees.models import FeePayment
from apps.results.models import Result
from apps.assignments.models import Assignment, AssignmentSubmission
from apps.library.models import Book, BookIssue
from apps.leave.models import LeaveApplication


class DashboardAnalyticsView(APIView):
    """Dashboard analytics"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Student statistics
        total_students = Student.objects.filter(is_active=True).count()
        
        # Staff statistics
        total_staff = Staff.objects.filter(status='active').count()
        
        # Attendance statistics (last 30 days)
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        total_attendance = Attendance.objects.filter(date__gte=thirty_days_ago).count()
        present_count = Attendance.objects.filter(date__gte=thirty_days_ago, status='present').count()
        attendance_percentage = round((present_count / total_attendance * 100), 2) if total_attendance > 0 else 0
        
        # Fee statistics
        total_fees = FeePayment.objects.aggregate(total=Sum('amount'))['total'] or 0
        paid_fees = FeePayment.objects.filter(status='paid').aggregate(total=Sum('amount'))['total'] or 0
        pending_fees = total_fees - paid_fees
        
        # Assignment statistics
        total_assignments = Assignment.objects.filter(status='published').count()
        pending_submissions = AssignmentSubmission.objects.filter(status='pending').count()
        
        # Library statistics
        total_books = Book.objects.count()
        issued_books = BookIssue.objects.filter(status='issued').count()
        
        return Response({
            'students': {
                'total': total_students,
            },
            'staff': {
                'total': total_staff,
            },
            'attendance': {
                'percentage': attendance_percentage,
                'present': present_count,
                'total': total_attendance,
            },
            'fees': {
                'total': float(total_fees),
                'paid': float(paid_fees),
                'pending': float(pending_fees),
            },
            'assignments': {
                'total': total_assignments,
                'pending_submissions': pending_submissions,
            },
            'library': {
                'total_books': total_books,
                'issued_books': issued_books,
            }
        })


class StudentAnalyticsView(APIView):
    """Student analytics"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Grade-wise distribution
        grade_distribution = Student.objects.filter(is_active=True).values('grade').annotate(count=Count('id')).order_by('grade')
        
        # Gender distribution
        gender_distribution = Student.objects.filter(is_active=True).values('gender').annotate(count=Count('id'))
        
        # Recent admissions (last 30 days)
        thirty_days_ago = timezone.now().date() - timedelta(days=30)
        recent_admissions = Student.objects.filter(admission_date__gte=thirty_days_ago).count()
        
        return Response({
            'grade_distribution': list(grade_distribution),
            'gender_distribution': list(gender_distribution),
            'recent_admissions': recent_admissions,
        })


class AttendanceAnalyticsView(APIView):
    """Attendance analytics"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Last 7 days attendance
        seven_days_ago = timezone.now().date() - timedelta(days=7)
        daily_attendance = []
        
        for i in range(7):
            date = seven_days_ago + timedelta(days=i)
            total = Attendance.objects.filter(date=date).count()
            present = Attendance.objects.filter(date=date, status='present').count()
            daily_attendance.append({
                'date': date.strftime('%Y-%m-%d'),
                'total': total,
                'present': present,
                'percentage': round((present / total * 100), 2) if total > 0 else 0
            })
        
        # Status-wise distribution
        status_distribution = Attendance.objects.values('status').annotate(count=Count('id'))
        
        return Response({
            'daily_attendance': daily_attendance,
            'status_distribution': list(status_distribution),
        })


class FeeAnalyticsView(APIView):
    """Fee analytics"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Payment status distribution
        status_distribution = FeePayment.objects.values('status').annotate(
            count=Count('id'),
            total_amount=Sum('amount')
        )
        
        # Monthly collection (last 6 months)
        six_months_ago = timezone.now().date() - timedelta(days=180)
        monthly_collection = FeePayment.objects.filter(
            payment_date__gte=six_months_ago,
            status='paid'
        ).extra(
            select={'month': 'strftime("%%Y-%%m", payment_date)'}
        ).values('month').annotate(total=Sum('amount')).order_by('month')
        
        return Response({
            'status_distribution': list(status_distribution),
            'monthly_collection': list(monthly_collection),
        })


class ResultAnalyticsView(APIView):
    """Result analytics"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Grade distribution
        grade_distribution = Result.objects.values('grade').annotate(count=Count('id'))
        
        # Average marks by subject
        subject_averages = Result.objects.values('subject__name').annotate(
            avg_marks=Avg('marks_obtained')
        ).order_by('-avg_marks')
        
        # Pass/Fail statistics
        total_results = Result.objects.count()
        passed = Result.objects.filter(grade__in=['A+', 'A', 'B+', 'B', 'C+', 'C', 'D']).count()
        failed = total_results - passed
        
        return Response({
            'grade_distribution': list(grade_distribution),
            'subject_averages': list(subject_averages),
            'pass_fail': {
                'total': total_results,
                'passed': passed,
                'failed': failed,
                'pass_percentage': round((passed / total_results * 100), 2) if total_results > 0 else 0
            }
        })
