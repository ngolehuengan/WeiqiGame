/* eslint-disable no-undef */
import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import classNames from 'classnames/bind';
import Button from '~/components/Button';
import styles from './Register.module.scss';

const cx = classNames.bind(styles);

function Register() {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const handleRegister = (e) => {
        e.preventDefault();

        if (password !== confirmPassword) {
            setErrorMessage('Mật khẩu không khớp.');
            return;
        }

        // Giả sử có một danh sách các tên tài khoản đã tồn tại
        const existingUsernames = ['user1', 'user2', 'user3'];

        if (existingUsernames.includes(username.toLowerCase())) {
            setErrorMessage('Tên tài khoản đã tồn tại.');
            return;
        }

        alert('Đăng ký thành công! Mời bạn đăng nhập.');
        navigate('/login');
    };

    return (
        <div className={cx('wrapper')}>
            <h2>Đăng ký</h2>
            <form onSubmit={(e) => handleRegister(e)}>
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
                <div className={cx('form-group')}>
                    <label htmlFor="confirmPassword">Nhập lại mật khẩu:</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        name="confirmPassword"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        placeholder="Nhập lại mật khẩu"
                        required
                    />
                </div>
                {errorMessage && <p className={cx('error-message')}>{errorMessage}</p>}
                <div className={cx('register-link')}>
                    <span>Đã có tài khoản? </span>
                    <Link to="/login">Đăng nhập</Link>
                </div>
                <Button type="submit">Đăng ký</Button>
            </form>
        </div>
    );
}

export default Register;
