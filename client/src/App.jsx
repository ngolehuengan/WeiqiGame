import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { routes } from '~/routes';

import { DefaultLayout } from '~/components/Layouts';
import { PrivateRoute } from '~/components/PrivateRoute';
import { AuthProvider } from '~/components/PrivateRoute/AuthContext';

function App() {
    return (
        <AuthProvider>
            <Router>
                <AppContent />
            </Router>
        </AuthProvider>
    );
}

function AppContent() {
    const navigate = useNavigate();

    useEffect(() => {
        const handleBeforeUnload = () => {
            sessionStorage.setItem('isPageRefresh', 'true');
        };

        window.addEventListener('beforeunload', handleBeforeUnload);

        return () => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        };
    }, []);

    useEffect(() => {
        if (sessionStorage.getItem('isPageRefresh') === 'true') {
            sessionStorage.removeItem('isPageRefresh');
            navigate('/');
        }
    }, [navigate]);

    return (
        <div className="App">
            <Routes>
                {routes.map((route, index) => {
                    const Layout = route.layout || DefaultLayout;
                    const isProtected = route.protected;

                    return (
                        <Route
                            key={index}
                            path={route.path}
                            element={
                                <Layout>
                                    {isProtected ? (
                                        <PrivateRoute>
                                            <route.component />
                                        </PrivateRoute>
                                    ) : (
                                        <route.component />
                                    )}
                                </Layout>
                            }
                        />
                    );
                })}
            </Routes>
        </div>
    );
}

export default App;
