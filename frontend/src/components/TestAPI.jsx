import React, { useState } from 'react';
import axios from 'axios';

const TestAPI = () => {
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const testConnection = async () => {
    setLoading(true);
    setResult('Testing...');
    
    try {
      // Test 1: Check if backend is reachable
      const response1 = await axios.get('http://localhost:8000/');
      setResult(prev => prev + '\n✅ Backend is reachable');
      
      // Test 2: Try login
      const response2 = await axios.post('http://localhost:8000/api/v1/auth/login/', {
        email: 'admin@school.com',
        password: 'admin123'
      });
      
      setResult(prev => prev + '\n✅ Login API works!');
      setResult(prev => prev + '\n✅ Response: ' + JSON.stringify(response2.data, null, 2));
      
    } catch (error) {
      setResult(prev => prev + '\n❌ Error: ' + error.message);
      if (error.response) {
        setResult(prev => prev + '\n❌ Response data: ' + JSON.stringify(error.response.data, null, 2));
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">API Connection Test</h1>
      <button 
        onClick={testConnection}
        disabled={loading}
        className="bg-blue-500 text-white px-4 py-2 rounded"
      >
        {loading ? 'Testing...' : 'Test API Connection'}
      </button>
      <pre className="mt-4 p-4 bg-gray-100 rounded whitespace-pre-wrap">
        {result}
      </pre>
    </div>
  );
};

export default TestAPI;
