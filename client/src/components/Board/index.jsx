/* eslint-disable react/prop-types */
import { useEffect, useRef } from 'react';
import classNames from 'classnames/bind';
import styles from './Board.module.scss';
import images from '~/assets/images';

const cx = classNames.bind(styles);

function Board({ size }) {
    const gameBoardRef = useRef(null);
    useEffect(() => {
        const handleUnload = (event) => {
            if (window.confirm()) {
                return true;
            }
            event.preventDefault();
            return false;
        };

        window.addEventListener('beforeunload', handleUnload);

        return () => {
            window.removeEventListener('beforeunload', handleUnload);
        };
    }, []);
    useEffect(() => {
        const gameBoard = gameBoardRef.current;
        let isBlackTurn = true;
        const alphabet = 'ABCDEFGHJKLMNOPQRST';
        let iskoMove = false;
        let koPoint = [-1, -1];
        if (!gameBoard) {
            console.error("Element with class 'goBoard' not found.");
            return;
        }
        setupBoard();

        let boardCellsArray = new Array(size);
        fillBoardCellsArray(boardCellsArray);
        function fillBoardCellsArray(array) {
            for (let i = 0; i < size; i++) {
                array[i] = new Array(size);
            }
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    array[i][j] = 0;
                }
            }
        }

        function setupBoard() {
            gameBoard.style.gridTemplateColumns = `repeat(${size + 2}, 1fr)`;
            addColumnCoordinates();
            let temp = size > 9 ? 1 : 0;
            for (let i = 0; i < size; i++) {
                for (let j = -1; j < size + 1; j++) {
                    if (j < size && i < size && j > -1) {
                        let cell = document.createElement('div');
                        cell.classList.add(styles.cell);
                        cell.id = j.toString() + (size - i - 1).toString();
                        let horizontalLine = document.createElement('div');
                        let verticalLine = document.createElement('div');
                        horizontalLine.className = `${styles.line} ${styles.horizontal}`;
                        verticalLine.className = `${styles.line} ${styles.vertical}`;
                        if (j == 0) {
                            horizontalLine.style.left = '50%';
                            horizontalLine.style.width = '50%';
                        }
                        if (j == size - 1) {
                            horizontalLine.style.right = '50%';
                            horizontalLine.style.width = '50%';
                        }
                        if (i == 0) {
                            verticalLine.style.top = '50%';
                            verticalLine.style.height = '50%';
                        }
                        if (i == size - 1) {
                            verticalLine.style.bottom = '50%';
                            verticalLine.style.height = '50%';
                        }
                        if (
                            (j == 2 + temp &&
                                (i == j || i == (size - 1) / 2 || i == size - temp - 3)) ||
                            (j == (size - 1) / 2 &&
                                (i == 2 + temp || i == size - temp - 3 || i == (size - 1) / 2)) ||
                            (j == size - temp - 3 &&
                                (i == 2 + temp || i == (size - 1) / 2 || i == j))
                        ) {
                            addStarPoint(cell);
                        }
                        cell.appendChild(horizontalLine);
                        cell.appendChild(verticalLine);
                        gameBoard.appendChild(cell);
                        cell.addEventListener('click', insertPiece);
                    }
                    if (j == -1 || j == size) {
                        addRowCoordinate(size - i);
                    }
                }
            }
            addColumnCoordinates();
        }

        function insertPiece(event) {
            let clickedSquare = event.target;

            if (clickedSquare.classList.contains(styles.piece) || clickedSquare.tagName == 'IMG') {
                return;
            }

            if (
                clickedSquare.classList.contains(styles.line) ||
                clickedSquare.classList.contains(styles.star)
            ) {
                clickedSquare = clickedSquare.parentNode;
            }
            let clickedSquareX = parseInt(clickedSquare.id.charAt(0));
            let clickedSquareY = parseInt(clickedSquare.id.charAt(1));
            let clickedSquareCoordinates = [clickedSquareX, clickedSquareY];
            let pieceColor = isBlackTurn ? 1 : 2;
            boardCellsArray[clickedSquareX][clickedSquareY] = pieceColor;
            let captures = checkCaptures(boardCellsArray, [clickedSquareX, clickedSquareY]);
            if (captures.length > 0) {
                if (!isValidCaptureMove(captures, clickedSquareCoordinates)) {
                    boardCellsArray[clickedSquareX][clickedSquareY] = 0;
                    captures.length = 0;
                    let alertMessage =
                        iskoMove && clickedSquareCoordinates.every((v, i) => v === koPoint[i])
                            ? 'Nước đi không hợp lệ do vi phạm luật Ko!'
                            : 'Không được phép thực hiện nước đi tự bắt quân!';
                    showAlert(alertMessage);
                    return;
                }
                captures.forEach(([x, y]) => removePiece(x, y));
                updateBoardArray(captures);
            }
            if (captures.length === 0) {
                iskoMove = false;
            }

            let color = isBlackTurn ? 'black' : 'white';
            var piece = document.createElement('div');
            piece.className = `${styles.piece} ${styles.color}`;
            let pieceImage = document.createElement('img');
            pieceImage.src = images[color];
            piece.appendChild(pieceImage);
            clickedSquare.appendChild(piece);
            isBlackTurn = !isBlackTurn;
        }
        function addColumnCoordinates() {
            for (let i = 0; i < size + 2; i++) {
                let coord = document.createElement('div');
                coord.classList.add(styles.coords);
                if (i > 0 && i < size + 1) coord.innerHTML = alphabet[i - 1];
                gameBoard.appendChild(coord);
            }
        }

        function addRowCoordinate(rowLabel) {
            let coord = document.createElement('div');
            coord.classList.add(styles.coords);
            coord.innerHTML = rowLabel;
            gameBoard.appendChild(coord);
        }

        function addStarPoint(cell) {
            let starPoint = document.createElement('div');
            starPoint.className = styles.star;
            starPoint.innerHTML = '•';
            cell.appendChild(starPoint);
        }

        function checkCaptures(board, lastMove) {
            let captures = [];
            let visited = Array(board.length)
                .fill()
                .map(() => Array(board.length).fill(false));
            let dx = [-1, 0, 1, 0];
            let dy = [0, 1, 0, -1];

            for (let i = 0; i < board.length; i++) {
                for (let j = 0; j < board.length; j++) {
                    if (board[i][j] !== 0 && !visited[i][j]) {
                        let capturedGroup = bfs(i, j, board, visited);
                        captures.push(...capturedGroup);
                    }
                }
            }
            if (lastMove) {
                let [x, y] = lastMove;
                for (let i = 0; i < 4; i++) {
                    let nx = x + dx[i];
                    let ny = y + dy[i];
                    if (
                        nx > 0 &&
                        ny >= 0 &&
                        nx < board.length &&
                        ny < board.length &&
                        board[nx][ny] !== 0 &&
                        !visited[nx][ny]
                    ) {
                        let capturedGroup = bfs(nx, ny, board, visited);
                        captures.push(...capturedGroup);
                    }
                }
            }
            return captures;
        }

        function bfs(x, y, board, visited) {
            let dx = [-1, 0, 1, 0];
            let dy = [0, 1, 0, -1];
            let color = board[x][y];
            let queue = [[x, y]];
            let group = [[x, y]];
            visited[x][y] = true;
            let hasLiberty = false;

            while (queue.length > 0) {
                let [cx, cy] = queue.shift();
                for (let i = 0; i < 4; i++) {
                    let nx = cx + dx[i];
                    let ny = cy + dy[i];
                    if (
                        nx >= 0 &&
                        ny >= 0 &&
                        nx < board.length &&
                        ny < board.length &&
                        !visited[nx][ny]
                    ) {
                        if (board[nx][ny] === color) {
                            queue.push([nx, ny]);
                            group.push([nx, ny]);
                            visited[nx][ny] = true;
                        } else if (board[nx][ny] === 0) {
                            hasLiberty = true;
                        }
                    }
                }
            }

            return hasLiberty ? [] : group;
        }

        function removePiece(x, y) {
            let squareId = x.toString() + y.toString();
            let square = document.getElementById(squareId);
            let children = square.childNodes;
            for (let i = children.length - 1; i >= 0; i--) {
                if (
                    !children[i].classList.contains(styles.line) &&
                    !children[i].classList.contains(styles.star)
                ) {
                    square.removeChild(children[i]);
                }
            }
        }

        function updateBoardArray(captures) {
            let turn = isBlackTurn ? 1 : 2;
            captures.forEach((element) => {
                if (turn != boardCellsArray[element[0]][element[1]])
                    boardCellsArray[element[0]][element[1]] = 0;
            });
        }

        function isValidCaptureMove(captures, clickedSquareCoordinates) {
            let colors = [];
            captures.forEach((element) => {
                let x = element[0];
                let y = element[1];
                let color = boardCellsArray[x][y];
                colors.push(color);
            });
            let allCapturedSameColor = colors.every((element) => element === colors[0]);
            let selfCapture = (isBlackTurn && colors[0] == 1) || (!isBlackTurn && colors[0] == 2);
            if (allCapturedSameColor && selfCapture) return false;
            let turn = isBlackTurn ? 1 : 2;
            if (
                !allCapturedSameColor &&
                iskoMove &&
                clickedSquareCoordinates[0] == koPoint[0] &&
                clickedSquareCoordinates[1] == koPoint[1]
            ) {
                return false;
            }
            iskoMove = !allCapturedSameColor;
            captures.forEach((element) => {
                if (turn != boardCellsArray[element[0]][element[1]]) {
                    clickedSquareCoordinates = element;
                }
            });
            koPoint = iskoMove ? clickedSquareCoordinates : [-1, 1];
            return true;
        }

        function showAlert(message) {
            alert(message);
        }
    }, [size]);
    return <div ref={gameBoardRef} className={cx('goBoard')}></div>;
}

export default Board;
