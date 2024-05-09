import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { routes } from '~/routes';

import { DefaultLayout } from '~/components/Layouts';
import { PrivateRoute } from '~/components/PrivateRoute';
import { AuthProvider } from '~/components/PrivateRoute/AuthContext';

function App() {
    return (
        <AuthProvider>
            <Router>
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
            </Router>
        </AuthProvider>
    );
}

export default App;
