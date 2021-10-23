class SummerCamp {
    constructor(organizer, location) {
        this.organizer = organizer;
        this.location = location;
        this.priceForTheCamp = {
            'child': 150,
            'student': 300,
            'collegian': 500,
        };
        this.listOfParticipants = [];
    }

    registerParticipant(name, condition, money) {
        if (!(condition in this.priceForTheCamp)) {
            throw new Error('Unsuccessful registration at the camp.');
        }

        if (this.findPersonIndex(name) != -1) {
            return `The ${name} is already registered at the camp.`;
        }

        const neededMoney = this.priceForTheCamp[condition];
        if (money < neededMoney) {
            return 'The money is not enough to pay the stay at the camp.';
        }

        const newParticipant = {
            name,
            condition,
            power: 100,
            wins: 0,
        };
        
        this.listOfParticipants.push(newParticipant);
        return `The ${name} was successfully registered.`;
    }

    findPersonIndex(name) {
        return this.listOfParticipants.findIndex(p => p.name == name);
    }

    unregisterParticipant(name) {
        const searchedParticipantIndex = this.findPersonIndex(name);
        
        if (searchedParticipantIndex == -1) {
            throw new Error(`The ${name} is not registered in the camp.`);
        }

        this.listOfParticipants.splice(searchedParticipantIndex, 1);
        return `The ${name} removed successfully.`;
    }

    timeToPlay(typeOfGame, participant1, participant2) {
        if (typeOfGame == 'WaterBalloonFights') {
            return this.waterBalloonFights(participant1, participant2);
        } else if (typeOfGame == 'Battleship') {
            return this.battleShip(participant1);
        }
        
    }

    waterBalloonFights(firstParticipantName, secondParticipantName) {
        const firstParticipantIndex = this.findPersonIndex(firstParticipantName);
        const secondParticipantIndex = this.findPersonIndex(secondParticipantName);

        if (firstParticipantIndex == -1 || secondParticipantIndex == -1) {
            throw new Error('Invalid entered name/s.');
        }

        const firstParticipant = this.listOfParticipants[firstParticipantIndex];
        const secondParticipant = this.listOfParticipants[secondParticipantIndex];
        
        if (firstParticipant.condition != secondParticipant.condition) {
            throw new Error('Choose players with equal condition.');
        }

        let winner;
        if (firstParticipant.power > secondParticipant.power) {
            firstParticipant.wins += 1
            winner = firstParticipant.name;
        } else if (firstParticipant.power < secondParticipant.power) {
            secondParticipant.wins += 1;
            winner = secondParticipant.name;
        } else {
            return 'There is no winner.'
        }

        return `The ${winner} is winner in the game WaterBalloonFights.`
    }

    battleShip(participantName) {
        const participantIndex = this.findPersonIndex(participantName);
        
        if (participantIndex == -1) {
            throw new Error('Invalid entered name/s.');
        }

        const participant = this.listOfParticipants[participantIndex];
        participant.power += 20;

        return `The ${participantName} successfully completed the game Battleship.`
    }

    toString() {
        const result = [
            `${this.organizer} will take ${this.listOfParticipants.length} participants on camping to ${this.location}`
        ];

        for (const participant of this.listOfParticipants.sort((a, b) => b.wins - a.wins)) {
            result.push(`${participant.name} - ${participant.condition} - ${participant.power} - ${participant.wins}`);
        }

        return result.join('\n');
    }
}
