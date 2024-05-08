/* eslint-disable react/prop-types */
import { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from './AuthContext';

const PrivateRoute = ({ children }) => {
    const auth = useContext(AuthContext);
    const isLoggedIn = auth ? auth.isLoggedIn : false;

    return isLoggedIn ? children : <Navigate to="/login" replace />;
};

export { PrivateRoute };
