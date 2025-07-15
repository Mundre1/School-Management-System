import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../services/api';

const ResultsList = () => {
  const navigate = useNavigate();
  const [results, setResults] = useState([]);
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedExam, setSelectedExam] = useState('');
  const [stats, setStats] = useState(null);

  useEffect(() => {
    fetchExams();
  }, []);

  useEffect(() => {
    if (selectedExam) {
      fetchResults();
      fetchStats();
    }
  }, [selectedExam]);

  const fetchExams = async () => {
    try {
      const response = await api.get('/results/exams/');
      setExams(response.data.results || response.data);
      if (response.data.length > 0 || response.data.results?.length > 0) {
        setSelectedExam((response.data.results || response.data)[0].id);
      }
    } catch (error) {
      console.error('Error fetching exams:', error);
    }
  };

  const fetchResults = async () => {
    try {
      setLoading(true);
      const response = await api.get('/results/results/', {
        params: { exam: selectedExam }
      });
      setResults(response.data.results || response.data);
    } catch (error) {
      console.error('Error fetching results:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchStats = async () => {
    try {
      const response = await api.get('/results/results/statistics/', {
        params: { exam: selectedExam }
      });
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching stats:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">Results Management</h1>
              <p className="text-sm text-gray-600">View and manage exam results</p>
            </div>
            <button
              onClick={() => navigate('/dashboard')}
              className="bg-gray-500 hover:bg-gray-600 text-white px-4 py-2 rounded-md text-sm font-medium transition"
            >
              ← Back to Dashboard
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Statistics Cards */}
        {stats && (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-white rounded-lg shadow p-6 border-l-4 border-blue-500">
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-gray-500 text-sm">Total Results</p>
                  <p className="text-3xl font-bold text-gray-800 mt-2">{stats.total_results || 0}</p>
                </div>
                <div className="text-4xl">📊</div>
              </div>
            </div>

            <div className="bg-white rounded-lg shadow p-6 border-l-4 border-green-500">
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-gray-500 text-sm">Pass Count</p>
                  <p className="text-3xl font-bold text-gray-800 mt-2">{stats.pass_count || 0}</p>
                </div>
                <div className="text-4xl">✅</div>
              </div>
            </div>

            <div className="bg-white rounded-lg shadow p-6 border-l-4 border-red-500">
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-gray-500 text-sm">Fail Count</p>
                  <p className="text-3xl font-bold text-gray-800 mt-2">{stats.fail_count || 0}</p>
                </div>
                <div className="text-4xl">❌</div>
              </div>
            </div>

            <div className="bg-white rounded-lg shadow p-6 border-l-4 border-purple-500">
              <div className="flex justify-between items-center">
                <div>
                  <p className="text-gray-500 text-sm">Average %</p>
                  <p className="text-3xl font-bold text-gray-800 mt-2">
                    {stats.average_percentage ? stats.average_percentage.toFixed(2) : 0}%
                  </p>
                </div>
                <div className="text-4xl">📈</div>
              </div>
            </div>
          </div>
        )}

        {/* Exam Selector */}
        <div className="bg-white rounded-lg shadow p-4 mb-6">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Select Exam
          </label>
          <select
            value={selectedExam}
            onChange={(e) => setSelectedExam(e.target.value)}
            className="w-full md:w-96 px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          >
            <option value="">Select an exam</option>
            {exams.map((exam) => (
              <option key={exam.id} value={exam.id}>
                {exam.name} - Grade {exam.grade} ({exam.exam_type})
              </option>
            ))}
          </select>
        </div>

        {/* Results Table */}
        <div className="bg-white rounded-lg shadow overflow-hidden">
          {!selectedExam ? (
            <div className="text-center py-12">
              <p className="text-gray-600 text-lg">Please select an exam to view results</p>
            </div>
          ) : loading ? (
            <div className="text-center py-12">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
              <p className="mt-4 text-gray-600">Loading results...</p>
            </div>
          ) : results.length === 0 ? (
            <div className="text-center py-12">
              <p className="text-gray-600 text-lg">No results found for selected exam</p>
              <p className="text-sm text-gray-500 mt-2">Results will appear here once published</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50 border-b">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Student
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Subject
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Marks Obtained
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Total Marks
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Percentage
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Grade
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {results.map((result) => (
                    <tr key={result.id} className="hover:bg-gray-50 transition">
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="text-sm font-medium text-gray-900">
                          {result.student_details?.first_name} {result.student_details?.last_name}
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                        {result.subject_details?.name}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-semibold">
                        {result.marks_obtained}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                        {result.total_marks}
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-semibold">
                        {parseFloat(result.percentage).toFixed(2)}%
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`px-3 py-1 inline-flex text-sm leading-5 font-bold rounded-full ${
                          result.grade === 'A+' || result.grade === 'A'
                            ? 'bg-green-100 text-green-800'
                            : result.grade.startsWith('B')
                            ? 'bg-blue-100 text-blue-800'
                            : result.grade.startsWith('C')
                            ? 'bg-yellow-100 text-yellow-800'
                            : result.grade === 'D'
                            ? 'bg-orange-100 text-orange-800'
                            : 'bg-red-100 text-red-800'
                        }`}>
                          {result.grade}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResultsList;
