import { Link, useNavigate } from 'react-router-dom';
import classNames from 'classnames/bind';
import Button from '~/components/Button';
import styles from './Home.module.scss';
import { PrivateRoute } from '~/components/PrivateRoute';
import { useContext } from 'react';
import { AuthContext } from '~/components/PrivateRoute/AuthContext';

const cx = classNames.bind(styles);

function Home() {
    const { logOut } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogOut = () => {
        logOut();
        navigate('/login');
    };

    return (
        <PrivateRoute>
            <div className={cx('wrapper')}>
                <Button>
                    <Link to="/play">Chơi</Link>
                </Button>
                <Button>
                    <Link to="/create-room">Tạo phòng</Link>
                </Button>
                <Button primary onClick={handleLogOut}>Đăng xuất</Button>
            </div>
        </PrivateRoute>
    );
}

export default Home;
