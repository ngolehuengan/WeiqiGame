import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classNames from 'classnames/bind';
import Button from '~/components/Button';
import styles from './Login.module.scss';
import { AuthContext } from '~/components/PrivateRoute/AuthContext';
import { useContext } from 'react';

const cx = classNames.bind(styles);

function Login() {
    const navigate = useNavigate();
    const { setIsLoggedIn } = useContext(AuthContext);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();

        // Giả định một yêu cầu API để xác thực thông tin đăng nhập
        const validUsers = [
            { username: 'admin', password: '123456' },
            { username: 'q', password: 'q' },
        ];

        const user = validUsers.find((u) => u.username === username && u.password === password);

        if (!user) {
            setErrorMessage('Tài khoản hoặc mật khẩu không chính xác.');
            return;
        }

        alert('Đăng nhập thành công!');
        setIsLoggedIn(true);
        navigate('/');
    };

    return (
        <div className={cx('wrapper')}>
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
    );
}

export default Login;
