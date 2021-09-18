function checkDistance(
    firstPointX, 
    firstPointY,
    secondPointX,
    secondPointY) {
    
    class Point {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }
    }

    class Distance {
        constructor(primaryPoint, otherPoint) {
            this.primaryPoint = primaryPoint;
            this.otherPoint = otherPoint;
        }

        getDistance() {
            let xDiff = Math.abs(this.primaryPoint.x - this.otherPoint.x);
            let yDiff = Math.abs(this.primaryPoint.y - this.otherPoint.y);
        
            let distance = Math.sqrt(xDiff ** 2 + yDiff ** 2);
            let status;

            if (distance % 1 == 0) {
                status = 'valid';
            } else {
                status = 'invalid';
            }

            return `{${this.primaryPoint.x}, ${this.primaryPoint.y}} to ` + 
                    `{${this.otherPoint.x}, ${this.otherPoint.y}} ` +
                    `is ${status}`;
        }
    }

    let originPoint = new Point(0, 0);
    let firstPoint = new Point(firstPointX, firstPointY);
    let secondPoint = new Point(secondPointX, secondPointY);

    let searchedDistances = [
        [firstPoint, originPoint],
        [secondPoint, originPoint],
        [firstPoint, secondPoint],
    ];
    
    for (let points of searchedDistances) {
        let distance = new Distance(points[0], points[1]);
        console.log(distance.getDistance());
    }
}

checkDistance(2, 1, 1, 1);