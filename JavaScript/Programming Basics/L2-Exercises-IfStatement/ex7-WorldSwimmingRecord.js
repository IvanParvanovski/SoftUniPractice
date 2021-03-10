function main(input)
{
    let recordInSeconds = Number(input[0]);
    let distanceInMeters = Number(input[1]);
    let timeInSecondsForOneMeter = Number(input[2]);

    let totalTime = distanceInMeters * timeInSecondsForOneMeter;
    let waterResistance = Math.floor(distanceInMeters / 15) * 12.5;

    totalTime += waterResistance;

    let result;
    if (totalTime < recordInSeconds)
        result = `Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`;
    else
        result = `No, he failed! He was ${(totalTime - recordInSeconds).toFixed(2)} seconds slower.`

    console.log(result);
}

main((["55555.67",
"3017",
"5.03"])
);
