/* jshint esversion: 6 */
/* jshint node: true */

'use strict';

class Item{
    constructor(name,quantity,price,store,section,priority) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
        this.store = store;
        this.section = section;
        this.priority = priority;
        this.property_purchased = false;

    }
    get property_purchased() {
        return this.property_purchased;
    }

    set property_purchased(new_value) {
        this.property_purchased = new_value;
}
}
class Subject {

    constructor() {
        this.handlers = []
    }

    subscribe(fn) {
            this.handlers.push(fn);
        }

    unsubscribe(fn) {
        this.handlers = this.handlers.filter(
            function(item) {
                if (item !== fn) {
                    return item;
                }
            }
        );
    }

    publish(msg, someobj) {
        var scope = someobj || window;
        for (let fn of this.handlers) {
            fn(scope, msg)
        }
    }
}

class shoppingList extends Subject{
    constructor() {
        super()
        this.items = [];
    }

    addItem(it){
        this.items.push(it);
    }
    cleanList(){
        //clears all purchased items from current list
        this.items.splice(0,this.items.length);

    }
    emptyList(){
        this.items = [];
    }
}

