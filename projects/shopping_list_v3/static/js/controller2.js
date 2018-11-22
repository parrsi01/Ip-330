/* jshint esversion: 6 */
/* jshint node: true */

'use strict';

var stores = ['Fareway', 'Ace Hardware', 'Caseys', 'The Hatchery', 'Amundsens'];
var sections = ['Produce', 'Meats', 'Cereal', 'Canned Goods', 'Frozen Foods', 'Dairy', 'Liquor', 'Tools', 'Clothing'];
var qty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var priority = ['low', 'medium', 'high'];
var shoppingModel = new ShoppingList();
var myView = new ShoppingView(shoppingModel);


function clickedon() {
    
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority'];
    let vals = {}
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price);

    shoppingModel.addItem(it);
}

function addList(){

    let savedcols = localStorage.getItem('item');
    savedcols = savedcols ? JSON.parse(savedcols) : [];
    let item_info = ['itemname', 'qty', 'store', 'category', 'price', 'priority'];
    let new_item = {};
    for (let cid of item_info) {
        new_item[cid] = document.getElementById('item_' + cid).value;
    }
    savedcols.push(new_item);
    window.localStorage.setItem('item', JSON.stringify(savedcols));
    console.log('item');
}


function saveList(){
    let savedcols = localStorage.getItem('item');
    savedcols = savedcols ? JSON.parse(savedcols) : [];
    localStorage.setItem('item', JSON.stringify(shoppingModel));
    console.log(JSON.stringify(shoppingModel));
    let item = localStorage.getItem('item');
    localStorage.setItem("shoppingModel",JSON.stringify(shoppingModel));
    console.log("save ShoppingList");
    console.log(item);
    let config = {}
	config.method = 'POST'
	config.body = JSON.stringify({'list': JSON.stringify(list.getShoppingList())})
	config.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
	fetch("/save", config)
}

function clearList(){
    ShoppingList.deleteRow(document.getElementById('shoppinglist'));
    let savedcols = localStorage.getItem('item');
    savedcols = savedcols ? localStorage.removeItem(shoppingModel) : [];
}


function clearItem(){
    ShoppingList.remove(document.getElementById('shoppingList'));
    let savedcols = localStorage.getItem('item');
    savedcols = savedcols ? localStorage.removeItem(shoppingModel) : [];

}

function populateSelect(selectId, sList) {
    let config = {}
	config.method = 'GET'
	config.body = JSON.stringify({'list': JSON.stringify(list.getShoppingList())})
	config.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
	fetch("/get", config)
    let sel = document.getElementById(selectId, sList);
    for (let s of sList) {
        
        let opt = document.createElement("option");
        opt.value = s;
        opt.innerHTML = s;
        sel.appendChild(opt);
    }
}

$(document).ready(function () {
    populateSelect('store', stores);
    populateSelect('category', sections);
    populateSelect('priority', priority);
    populateSelect('qty', qty);
   
})
