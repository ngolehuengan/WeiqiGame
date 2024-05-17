import { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classNames from 'classnames/bind';
import Button from '~/components/Button';
import styles from './Login.module.scss';
import { AuthContext } from '~/components/PrivateRoute/AuthContext';
import axios from 'axios';

const cx = classNames.bind(styles);

function Login() {
    const navigate = useNavigate();
    const { setIsLoggedIn } = useContext(AuthContext);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        
        try {
            const response = await axios.post('/api/login', {
                username,
                password,
            });

            const data = response.data;

            if (data.success) {
                alert(data.message);
                setIsLoggedIn(true);
                navigate('/');
            } else {
                setErrorMessage(data.message);
            }
        } catch (error) {
            if (error.response) {
                console.error('Error:', error.response.data);
                setErrorMessage(error.response.data.error);
            } else if (error.request) {
                console.error('No response received:', error.request);
                setErrorMessage('Không có phản hồi từ máy chủ. Vui lòng thử lại sau.');
            } else {
                console.error('Error:', error.message);
                setErrorMessage('Đã có lỗi xảy ra.');
            }
        }
    };

    return (
        <div className={cx('wrapper')}>
            <div className={cx('content')}>
                <h2>Đăng Nhập</h2>
                <form onSubmit={(e) => handleLogin(e)}>
                    <div className={cx('form-group')}>
                        <label htmlFor="username">Tài khoản:</label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Nhập tài khoản"
                            required
                        />
                    </div>
                    <div className={cx('form-group')}>
                        <label htmlFor="password">Mật khẩu:</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Nhập mật khẩu"
                            required
                        />
                    </div>
                    {errorMessage && <p className={cx('error-message')}>{errorMessage}</p>}
                    <div className={cx('register-link')}>
                        <span>Chưa có tài khoản? </span>
                        <Link to="/register">Đăng ký ngay!</Link>
                    </div>
                    <Button type="submit">Đăng Nhập</Button>
                </form>
            </div>
        </div>
    );
}

export default Login;
