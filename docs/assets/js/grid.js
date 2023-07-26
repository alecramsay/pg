// Common grid functionality

var centeredColumn = {
    headerClass: 'text-center',
    cellStyle: {
        textAlign: 'center',
    }
}

var rightJustifiedColumn = {
    headerClass: 'text-right',
    cellStyle: {
        textAlign: 'right',
    }
}

function numericComparator(val1, val2)
{
    return val1 - val2;
}

function numberWithCommas(x)
{
    n = Number(x.value)
    y = n.toLocaleString()

    // console.log(x, "=>", y)
    return y;
}

function percentage(x)
{
    n = Number(x.value) * 100
    y = n.toFixed(2).toString() + "%"

    // console.log(x, "=>", y)
    return y;
}
