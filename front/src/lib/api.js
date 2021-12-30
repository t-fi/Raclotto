export class Api {
    static async get(name, session) {
        let res = await fetch("api/" + name + "/?session_key=" + session);
        return await res.json();
    }

    static async validate(sessionKey) {
        let res = await fetch("api/sessions/validate/?session_key=" + sessionKey);
        return await res.json();
    }

    static async add(session, ingredient) {
        let res = await fetch("api/ingredients/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            redirect: 'follow',
            body: JSON.stringify(
                Object.assign({}, {session_key: session}, ingredient)
            )
        });
        return await res.json();
    }

    static async rate(session, pan, rating) {
        let res = await fetch("api/ratings/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            redirect: 'follow',
            body: JSON.stringify({
                session_key: session,
                pan: pan,
                user: this.getUser(),
                rating: rating
            })
        });
        return await res.json();
    }

    static async generate(session, numIngredient, numSauce) {
        let res = await fetch("api/generate/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            redirect: 'follow',
            body: JSON.stringify({
                session_key: session,
                user: this.getUser(),
                num_fill: numIngredient,
                num_sauce: numSauce,
                vegetarian: true,
                vegan: false,
                histamine: false,
                fructose: false,
                lactose: false,
                gluten: false
            })
        });
        return await res.json();
    }

    static async createSession(name) {
        let res = await fetch("api/sessions/create/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors', // no-cors, *cors, same-origin
            cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
            credentials: 'same-origin', // include, *same-origin, omit
            redirect: 'follow',
            body: JSON.stringify({ name: name })
        });
        return await res.json();
    }

    static getUser() {
        let user = "unknown";

        if (localStorage.getItem("name")) {
            user = localStorage.getItem("name");
        }

        return user;
    }
}