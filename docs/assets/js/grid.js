const centeredColumn = {
    headerClass: 'text-center',
    cellStyle: {
        textAlign: 'center',
    }
}

const rightJustifiedColumn = {
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

// District Cores Table

const coresColumns = [
    {headerName: 'ID', field: 'DISTRICT', width: 60, sortable: true, comparator: numericComparator, ...rightJustifiedColumn, unSortIcon: true},
    {headerName: 'Population', field: 'POPULATION', width: 120, valueFormatter: numberWithCommas, sortable: true, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...rightJustifiedColumn},
    {headerName: '% of District', field: 'DISTRICT%', width: 120, valueFormatter: percentage, sortable: true, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...rightJustifiedColumn},
    // {headerName: 'Cumulative %', field: 'CUMULATIVE%', width: 120, valueFormatter: percentage, ...rightJustifiedColumn},
];
