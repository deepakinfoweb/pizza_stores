    /*
        @#########    
        This is Pizza Type Start
        @#########  
    */
    //***********add neww pizza type start********
    function addNewPizzType() {
        var pizztype = document.getElementById("add_new_pizza_type_val").value;
        console.log(pizztype)
        if (pizztype) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#add_new_pizza_type').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("New Pizza Type have been created Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'createPizzaType' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "name": pizztype }));
        } else {
            document.getElementById("add_new_pizza_type_val").style.borderColor = "red"
            return;
        }
    }
    //***********add neww pizza type end********

    //***********open pizza type model start********
    function openeditpizzatypeModel(id, name) {
        console.log(id, " ", name)
        if (id && name) {
            document.getElementById('pizza_type_var').innerHTML = name;
            document.getElementById('pizza_type_id').value = id;
            $('#edit_pizza_type').modal('show')
        }
        else {
            return;
        }
    }

    function editPizzType() {
        var pizza_id = document.getElementById('pizza_type_id').value;
        var pizza_name = document.getElementById('new_edited_pizza_type').value;
        if (pizza_id && pizza_name) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#edit_pizza_type').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Edited Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'editpizzatype' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_type_id": pizza_id, "pizza_type_name": pizza_name }));
        } else {
            document.getElementById("new_edited_pizza_type").style.borderColor = "red"
            return;
        }
    }
    //***********open pizza type model end********

    function deletePizzaType(id) {
        console.log(id)
        if (id) {
            document.getElementById('delete_pizza_type_id').value = id;
            $('#delete_pizza_type').modal('show')
        }
        else {
            return;
        }
    }

    function delete_Pizza_Type_API() {
        var pizza_type_id = document.getElementById('delete_pizza_type_id').value;
        console.log("delete func ", pizza_type_id)
        if (pizza_type_id) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#delete_pizza_type').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Deleted Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'deletepizzatype' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_type_id": pizza_type_id }));
        } else {
            return;
        }
    }

    /*
    @#########  
      This is Pizza Size
    @#########  
    */

    //***********add neww pizza Size start********
    function addNewPizzSize() {
        var pizzasize = document.getElementById("add_new_pizza_size_val").value;
        // console.log(pizztype)
        if (pizzasize) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#add_new_pizza_size').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("New Pizza Type have been created Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'createPizzaSize' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "name": pizzasize }));
        } else {
            document.getElementById("add_new_pizza_size_val").style.borderColor = "red"
            return;
        }
    }
    //***********add neww pizza type end********

    //***********open pizza size model start********
    function openeditpizzasizeModel(id, name) {
        // console.log(id, " ", name)
        if (id && name) {
            document.getElementById('pizza_size_var').innerHTML = name;
            document.getElementById('pizza_size_id').value = id;
            $('#edit_pizza_size').modal('show')
        }
        else {
            return;
        }
    }

    function editPizzaSize() {
        var pizza_id = document.getElementById('pizza_size_id').value;
        var pizza_name = document.getElementById('new_edited_pizza_size').value;
        if (pizza_id && pizza_name) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#edit_pizza_size').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Edited Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'editpizzasize' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_size_id": pizza_id, "pizza_size_name": pizza_name }));
        } else {
            document.getElementById("new_edited_pizza_size").style.borderColor = "red"
            return;
        }
    }
    //***********open pizza size model end********

    function deletePizzaSize(id) {
        console.log(id)
        if (id) {
            document.getElementById('delete_pizza_size_id').value = id;
            $('#delete_pizza_size').modal('show')
        }
        else {
            return;
        }
    }

    function delete_Pizza_size_API() {
        var pizza_size_id = document.getElementById('delete_pizza_size_id').value;
        if (pizza_size_id) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#delete_pizza_size').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Deleted Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'deletepizzasize' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_size_id": pizza_size_id }));
        } else {
            return;
        }
    }

    /*
    @#########  
      This is Pizza Toppings
    @#########  
    */
    //***********add neww pizza Size start********
    function addNewPizzTopping() {
        var pizzatopping = document.getElementById("add_new_pizza_toppings_val").value;
        // console.log(pizztype)
        if (pizzatopping) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#add_new_pizza_topping').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("New Pizza Type have been created Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'createPizzaToppings' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "toppings": pizzatopping }));
        } else {
            document.getElementById("add_new_pizza_toppings_val").style.borderColor = "red"
            return;
        }
    }
    //***********add neww pizza type end********


    //***********open pizza toping model start******
    function openeditpizzatoppingsModel(id, name) {
        console.log(id, " ", name)
        if (id && name) {
            document.getElementById('pizza_topping_var').innerHTML = name;
            document.getElementById('pizza_topping_id').value = id;
            $('#edit_pizza_topping').modal('show')
        }
        else {
            return;
        }
    }

    function editPizzaTopping() {
        var pizza_id = document.getElementById('pizza_topping_id').value;
        var pizza_name = document.getElementById('new_edited_pizza_topping').value;
        if (pizza_id && pizza_name) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#edit_pizza_topping').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Edited Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'editpizzatoppings' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_toppings_id": pizza_id, "toppings": pizza_name }));
        } else {
            document.getElementById("new_edited_pizza_topping").style.borderColor = "red"
            return;
        }
    }
    //***********open pizza size model end********

    //***********open pizza toping model start******
    function deletePizzaTopping(id) {
        console.log(id)
        if (id) {
            document.getElementById('delete_pizza_topping_id').value = id;
            $('#delete_pizza_topping').modal('show')
        }
        else {
            return;
        }
    }

    function delete_Pizza_topping_API() {
        var pizza_topping_id = document.getElementById('delete_pizza_topping_id').value;
        if (pizza_topping_id) {
            const xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 & this.status == 200) {
                    $('#delete_pizza_topping').modal('hide')
                    resp = JSON.parse(this.responseText).Status;
                    if (resp == "Success") {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Pizza have been Deleted Successfully.");
                        $('#messageModel').modal('show')
                    } else {
                        $('#messageHeader').html("");
                        $('#messageBody').html("Something went wrong please try again later.");
                        $('#messageModel').modal('show')
                    }
                }
            };
            xmlhttp.open("POST", "{% url 'deletepizzatoppings' %}", true);
            xmlhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(JSON.stringify({ "pizza_toppings_id": pizza_topping_id }));
        } else {
            return;
        }
    }

    /*
    @#########  
      Make your own pizza function
    @#########  
    */
    function make_own_pizza() {
        var pizza_type = document.getElementById('own_pizza_type_id').value;
        var pizza_size = document.getElementById('own_pizza_size_id').value;
        var pizza_toppings = document.getElementById('own_pizza_toppings_id').value;
        if (pizza_type && pizza_size && pizza_toppings) {
            console.log(pizza_type, pizza_size, pizza_toppings)
        } else {
            if (!pizza_type) {
                document.getElementById('own_pizza_type_id').style.borderColor = "red"
                console.log('pizza type cant be empty ');
                return;
            } else if (!pizza_size) {
                document.getElementById('own_pizza_size_id').style.borderColor = "red"
                console.log('pizza size cant be empty ');
                return;
            } else {
                document.getElementById('own_pizza_toppings_id').style.borderColor = "red"
                console.log('pizza toppings cant be empty ');
                return;
            }
        }
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
