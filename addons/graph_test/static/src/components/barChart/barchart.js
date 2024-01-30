/** @odoo-module **/
// import { registry } from "@web/core/registry"
// import { loadJS } from "@web/core/assets"
// import { Component, onWillStart, useRef, onMounted } from "@odoo/owl";

// export class BarChartComponent extends Component {
//     static template =  "graph_test.BarChartComponent";

//     setup(){
//         super.setup()
//         console.log("hola!!!")

//     }
// }

const { Component, mount, xml } = owl;

class BarChartComponent extends Component {
    static template = 'graph_test.BarChart_x_Component';

    setup(){
         console.log("hola!!!");    
        };
};

mount(BarChartComponent, document.body, { dev: true });
