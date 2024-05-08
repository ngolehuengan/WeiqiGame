import { Link } from 'react-router-dom';
import classNames from 'classnames/bind';
import Button from '~/components/Button';
import styles from './Home.module.scss';
import { PrivateRoute } from '~/PrivateRoute';

const cx = classNames.bind(styles);

function Home() {
    return (
        <PrivateRoute>
            <div className={cx('wrapper')}>
                <Button>
                    <Link to="/play">Chơi</Link>
                </Button>
                <Button>
                    <Link to="/create-room">Tạo phòng</Link>
                </Button>
            </div>
        </PrivateRoute>
    );
}

export default Home;
