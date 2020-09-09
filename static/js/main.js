function fill(key, value) {

    /*
    <div class=card"' style=width: 18rem;">
    <img class="card-img-top" src="static/upload/images/test.png" alt="Card image cap">
            <div class="card-body">
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the
                    card's content.</p>
            </div>
        </div>
    ";*/

    prediction = value

    par = document.getElementById("cont");

    c = document.createElement('div')
    c.classList.add('card')
    c.classList.add('col-lg-5')
    c.style.padding = '0px'
    c.style.margin = '30px'

    im = document.createElement('img')
    im.classList.add('card-img-top')
    im.classList.add('col-lg-12')
    im.alt = 'card image cap'
    im.style.padding = '0px'
    im.setAttribute('src', 'data:image/png;base64,' + key);

    c2 = document.createElement('div')
    c2.classList.add('card-body')

    p = document.createElement('p')
    p.classList.add('card-text')
    p.classList.add('text-center')
    p.innerHTML = prediction // Prediction of the image 

    c2.appendChild(p)

    c.appendChild(im)
    c.appendChild(c2)

    par.appendChild(c)
}
if ('{{ message}}' != "Home") {
    var dat = JSON.parse('{{ message | tojson | safe}}')
    for (const [key, value] of Object.entries(dat)) {
        fill(key, value)
    }
}