/* eslint-disable react/prop-types */
import { createContext, useEffect, useState } from 'react';

const SESSION_STORAGE_KEY = 'isLoggedIn';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [isLoggedIn, setIsLoggedIn] = useState(() => {
        const storedValue = sessionStorage.getItem(SESSION_STORAGE_KEY);
        return storedValue === 'true';
    });

    const logOut = () => {
        setIsLoggedIn(false);
        sessionStorage.removeItem(SESSION_STORAGE_KEY);
    };

    useEffect(() => {
        sessionStorage.setItem(SESSION_STORAGE_KEY, isLoggedIn.toString());
    }, [isLoggedIn]);

    return (
        <AuthContext.Provider value={{ isLoggedIn, setIsLoggedIn, logOut }}>
            {children}
        </AuthContext.Provider>
    );
};

export { AuthContext, AuthProvider };
