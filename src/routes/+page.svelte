<script>
    async function get_stuff() {
        const target = "http://192.168.1.99:8000/";
        const response = await fetch(target);
        const payload = await response.json();
        return payload;
    }
</script>

<h1>API Call Testing</h1>
<span class="menu"><a href="/decompose">POST and GET</a></span>
<span class="menu"><a href="table">POST to Retrieve Tabular Data</a></span>
<div class="something">
    {#await get_stuff()}
        ...
    {:then payload}
        <h2>GET inline</h2>
        {payload.message}
    {/await}
</div>

<style>
    .something {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
    .menu {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
    .menu a:link {
        color: yellow;
        text-decoration: none;
    }
    .menu a:visited {
        color: white;
        text-decoration: none;
    }
</style>
