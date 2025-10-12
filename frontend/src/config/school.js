// School Configuration
export const SCHOOL_CONFIG = {
  name: 'Itahari International School',
  shortName: 'IIS',
  address: 'Itahari, Sunsari, Nepal',
  phone: '+977-25-XXXXXX',
  email: 'info@itahariinternational.edu.np',
  website: 'www.itahariinternational.edu.np',
  established: '2020',
  
  // Academic Configuration
  academic: {
    currentYear: '2025-2026',
    grades: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    sections: ['A', 'B', 'C', 'D'],
  },
  
  // System Configuration
  system: {
    version: '1.0.0',
    apiUrl: process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1',
  },
  
  // Theme Configuration
  theme: {
    primaryColor: '#2563eb',
    secondaryColor: '#7c3aed',
    accentColor: '#f59e0b',
  },
};

export default SCHOOL_CONFIG;
