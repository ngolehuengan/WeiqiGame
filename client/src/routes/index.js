import Home from '~/pages/Home';
import Login from '~/pages/Login';
import Register from '~/pages/Register';
import ActivityPlay from '../pages/ActivityPlay';

const routes = [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/play', component: ActivityPlay },
];

export { routes };
