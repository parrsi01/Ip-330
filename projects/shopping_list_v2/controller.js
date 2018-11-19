/* jshint esversion: 6 */
/* jshint node: true */

'use strict';

var shoppingModel = new shoppingList()

function clickedon() {
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority'];
    let vals = {};
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price);
    shoppingModel.addItem(it);
}

function selectItems(selectId, my_list) {
    let select = document.getElementById(selectId, my_list)
    for (let i of my_list) {
        let opt = document.createElement("option")
        opt.value = s;
        opt.innerHTML = s
        select.appendChild(opt)
    }
}

$(document).ready(function () {
    selectItems('store', stores)
    selectItems('category', sections)
})
