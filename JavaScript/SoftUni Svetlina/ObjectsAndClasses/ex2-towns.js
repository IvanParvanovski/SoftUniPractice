function towns(input) {
    for (const row of input) {
        const [town, latitude, longitude] = row.split(' | ');
        console.log({
            town,
            latitude: Number(latitude).toFixed(2),
            longitude: Number(longitude).toFixed(2),
        });
    }
}

towns(['Sofia | 42.696552 | 23.32601',
'Beijing | 39.913818 | 116.363625']);