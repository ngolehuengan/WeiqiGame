// import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import axios from 'axios';
import GlobalStyles from '~/components/GlobalStyles';

axios.defaults.baseURL = 'http://127.0.0.1:5000';
axios.defaults.headers.common['Content-Type'] = 'application/json; charset=utf-8';
axios.defaults.headers.common['Accept'] = 'application/json';
axios.defaults.responseType = 'json';

ReactDOM.createRoot(document.getElementById('root')).render(
    // <React.StrictMode>
    <GlobalStyles>
        <App />
    </GlobalStyles>,
    // </React.StrictMode>,
);
