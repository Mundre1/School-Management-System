import api from './api';

const authService = {
  login: async (email, password) => {
    try {
      console.log('Attempting login with:', email);
      const response = await api.post('/auth/login/', { email, password });
      console.log('Login response:', response);
      
      if (response.data.success) {
        const { access, refresh } = response.data.data.tokens;
        const user = response.data.data.user;
        
        localStorage.setItem('access_token', access);
        localStorage.setItem('refresh_token', refresh);
        localStorage.setItem('user', JSON.stringify(user));
        
        console.log('Login successful, tokens stored');
        return response.data;
      }
      throw new Error('Login failed - success flag is false');
    } catch (error) {
      console.error('Auth service error:', error);
      throw error;
    }
  },

  logout: async () => {
    try {
      const refreshToken = localStorage.getItem('refresh_token');
      await api.post('/auth/logout/', { refresh_token: refreshToken });
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      localStorage.removeItem('user');
    }
  },

  getCurrentUser: () => {
    const userStr = localStorage.getItem('user');
    return userStr ? JSON.parse(userStr) : null;
  },

  isAuthenticated: () => {
    return !!localStorage.getItem('access_token');
  },

  getProfile: async () => {
    const response = await api.get('/auth/profile/');
    return response.data;
  },
};

export default authService;
