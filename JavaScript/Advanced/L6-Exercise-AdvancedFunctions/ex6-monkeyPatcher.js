function monkeyPatcher(option) {

    function incrementVote() {
        this[option + 's'] += 1;
    }

    function getRating(balance) {
        let rating;
        let totalVotes = this.upvotes + this.downvotes;

        if (totalVotes < 10) {
            rating = 'new';
        } else if (this.upvotes > totalVotes * 0.66) {
            rating = 'hot';
        } else if (balance >= 0 && (this.upvotes > 100 || this.downvotes > 100)) {
            rating = 'controversial';
        } else if (balance < 0) {
            rating = 'unpopular';
        } else {
            rating = 'new';
        }

        return rating;
    }

    function getScore() {
        const result = [];
        const totalVotes = this.upvotes + this.downvotes;

        let resultUpVotes = this.upvotes;
        let resultDownVotes = this.downvotes;
        const balance = this.upvotes - this.downvotes;
        const rating = getRating.call(this, balance);

        if (totalVotes > 50) {
            const greaterValue = this.upvotes > this.downvotes ? this.upvotes : this.downvotes;
            const increase = Math.ceil(0.25 * greaterValue);

            resultUpVotes = this.upvotes + increase;
            resultDownVotes = this.downvotes + increase;
        }
        
        result.push(resultUpVotes, resultDownVotes);
        result.push(balance);
        result.push(rating);

        return result;
    }

    const commands = {
        'upvote': incrementVote,
        'downvote': incrementVote,
        'score': getScore,
    }

    return commands[option].bind(this)();  
}

var forumPost = {
    id: '1',
    author: 'pesho',
    content: 'hi guys',
    upvotes: 0,
    downvotes: 0
};

// var forumPost = {
//     id: '2',
//     author: 'gosho',
//     content: 'whats up?',
//     upvotes: 120,
//     downvotes: 30
// };

// var answer = monkeyPatcher.call(forumPost, 'score');
// console.log(answer);
// var expected = [150, 60, 90, 'hot'];

monkeyPatcher.call(forumPost, 'upvote');

var answer = monkeyPatcher.call(forumPost, 'score');
console.log(answer);
var expected = [1, 0, 1, 'new'];

// compareScore(expected, answer);

// function compareScore(expected, answer) {
//     expect(expected[0]).to.equal(answer[0], 'Incorrect number of upvotes');
//     expect(expected[1]).to.equal(answer[1], 'Incorrect number of downvotes');
//     expect(expected[2]).to.equal(answer[2], 'Incorrect score');
//     expect(expected[3]).to.equal(answer[3], 'Incorrect rating');
// }

// let post = {
//     id: '3',
//     author: 'emil',
//     content: 'wazaaaaa',
//     upvotes: 100,
//     downvotes: 100
// };

// monkeyPatcher.call(post, 'upvote');
// monkeyPatcher.call(post, 'downvote');
// let score = monkeyPatcher.call(post, 'score'); // [127, 127, 0, 'controversial']
// for (let i = 0; i < 50; i++) {
//     monkeyPatcher.call(post, 'downvote');         // (executed 50 times)
// }
// score = monkeyPatcher.call(post, 'score');     // [139, 189, -50, 'unpopular']
