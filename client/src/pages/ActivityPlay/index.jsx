import { useState } from 'react';
import classNames from 'classnames/bind';
import Board from '~/components/Board';
import Button from '~/components/Button';
import styles from './ActivityPlay.module.scss';

const cx = classNames.bind(styles);

const ActivityPlay = () => {
    const [boardSize, setBoardSize] = useState(null);
    const [showPopup, setShowPopup] = useState(true);

    const handleSizeChange = (size) => {
        setBoardSize(size);
        setShowPopup(false);
    };

    return (
        <div>
            {showPopup && (
                <div className={cx('popup-overlay')}>
                    <div className={cx('popup-content')}>
                        <h2>Select Board Size</h2>
                        <Button onClick={() => handleSizeChange(9)}>9x9</Button>
                        <Button onClick={() => handleSizeChange(13)}>13x13</Button>
                        <Button onClick={() => handleSizeChange(19)}>19x19</Button>
                    </div>
                </div>
            )}
            {boardSize && <Board size={boardSize} />}
        </div>
    );
};

export default ActivityPlay;
