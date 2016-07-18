openerp.uniit3 = function (instance) {

    var QWeb = instance.web.qweb;
    var _t = instance.web._t;
    var _lt = instance.web._lt;
    var sessions = new openerp.web.Model("temperature");
    var sessions2 = new openerp.web.Model("temperatures");
    var counter = 0
    window.refreshDiv = function() {
                counter = counter + 1;
                var temps = [];
                var last_update = ''
                sessions.call("search_read",[]).then(function(result){
                last_update = result[0]['last_update']
                })
                sessions2.call("search_read",[]).then(function(result){
                    for (i = 0; i < result.length; i++) {
                        if (result[i]['datos'] == last_update){
                            if (result[i]['units'] == "C"){
                                temps.push(result[i]);
                            }
                        }
                    }
                var temp_notifab =''
                var temp_notifc =''
                var temp_notifd =''
                var temp_notife =''
                for(i=0; i<temps.length; i++){
                    switch(temps[i]['name']){
                        case 'Room A/B -T':
                            temp_notifab = temp_notifab.concat('A/B: ',temps[i]['value'],'oC | ')
                            document.getElementById("test1").innerHTML = temp_notifab;
                            if (temps[i]['value']<temps[i]['min'] || temps[i]['value']>temps[i]['max'] ){
                                    document.getElementById("test1").style.color = "red";
                            }
                            else{
                                document.getElementById("test1").style.color = "green";
                            }
                            break;
                        case 'Room C -T':
                            temp_notifc = temp_notifc.concat('C: ',temps[i]['value'],'oC | ')
                            document.getElementById("test2").innerHTML = temp_notifc;
                            if (temps[i]['value']<temps[i]['min'] || temps[i]['value']>temps[i]['max'] ){
                                    document.getElementById("test2").style.color = "red";
                            }
                            else{
                                document.getElementById("test2").style.color = "green";
                            }
                            break;
                        case 'Freezer D -T':
                            temp_notifd = temp_notifd.concat('D: ',temps[i]['value'],'oC | ')
                            document.getElementById("test3").innerHTML = temp_notifd;
                            if (temps[i]['value']<temps[i]['min'] || temps[i]['value']>temps[i]['max'] ){
                                    document.getElementById("test3").style.color = "red";
                            }
                            else{
                                document.getElementById("test3").style.color = "green";
                            }
                            break;
                        case 'Cold Room E -T':
                            temp_notifd = temp_notifd.concat('E: ',temps[i]['value'],'oC | ')
                            document.getElementById("test4").innerHTML = temp_notifd;
                            if (temps[i]['value']<temps[i]['min'] || temps[i]['value']>temps[i]['max'] ){
                                    document.getElementById("test4").style.color = "red";
                            }
                            else{
                                document.getElementById("test4").style.color = "green";
                            }
                            break;
                    }
                }

               openerp.web.bus.trigger('resize');
                })

    }
    instance.uniit3.place_temperature = instance.web.Widget.extend({
        template: 'place_temperature',
        init: function (parent) {
            this._super(parent);
            window.setInterval("refreshDiv()", 60000);
        },
    });

    instance.web.UserMenu.include({
        do_update: function () {
            this._super();
            var self = this;
            var temperature = new openerp.web.Model('temperatures');
            this.update_promise.done(function () {
                if (!_.isUndefined(self.place_temperature)) {
                    return;
                }
            self.place_temperature = new instance.uniit3.place_temperature(self);
            self.place_temperature.appendTo(instance.webclient.$('.oe_systray'));
            });
        },
    });
};
