function main(input)
{
    let paintTins = Number(input[0]);
    let wallpapers = Number(input[1]);
    let priceForPairGloves = Number(input[2]);
    let priceForBrush = Number(input[3]);

    let paintPrice = 21.50;
    let wallpapersPrice = 5.20;

    let neededGloves = Math.ceil(0.35 * wallpapers);
    let neededBrushes = Math.floor(0.48 * paintTins);

    let total = paintTins * paintPrice + 
                wallpapers * wallpapersPrice + 
                neededGloves * priceForPairGloves +
                neededBrushes * priceForBrush;
    
    console.log(`This delivery will cost ${(1 / 15 * total).toFixed(2)} lv.`);

}


main([10, 8, 2.2, 5]);
