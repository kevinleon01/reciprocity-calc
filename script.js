function calculateReciprocity() {
    //initiate consts
    const portra400 = 1.35
    const pancro400 = 1.3
    const hp5 = 1.31
    const trix = 1.54
    const cinestill800t = 1.33
    const tmax400 = 1.24
    const tmax100 = 1.15
    const other = 1.33

    let filmstock = 0

    var shutterInput = document.getElementById('shutter').value
    const shutter = parseFloat(shutterInput)
    
    var filmStocks = document.querySelector('input[name="film-stock"]:checked').value;

    if (filmStocks === "portra400") {
        filmStock = portra400 
    } else if (filmStocks === "pancro400") {
        filmStock = pancro400
    } else if (filmStocks === "hp5") {
        filmStock = hp5
    }else if (filmStocks === "trix") {
        filmStock = trix
    }else if (filmStocks === "cinestill800t") {
        filmStock = cinestill800t
    }else if (filmStocks === "tmax400") {
        filmStock = tmax400
    }else if (filmStocks === "tmax100") {
        filmStock = tmax100
    }else if (filmStocks === "other") {
        filmStock = other
    }
    console.log(filmStock)
    
    if (shutter > 1) {
        let newTime = Math.pow(shutter, filmStock)
        let time = newTime.toFixed(2)
        document.getElementById("results").innerHTML = time + " seconds"
    } else {
        document.getElementById("results").innerHTML = "You don't need to account for reciprocity failure"
    }

}