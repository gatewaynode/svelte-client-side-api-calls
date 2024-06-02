<script>
    async function get_stuff() {
        const target = "http://192.168.1.99:8000/";
        const response = await fetch(target);
        const payload = await response.json();
        return payload;
    }
</script>

<h2>Inline Fetch with GET request.</h2>
<div class="something">
    {#await get_stuff()}
        ...
    {:then payload}
        <h3 class="label">GET inline</h3>
        {payload.message}
    {/await}
</div>

<style>
    .something {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
    .label {
        color: rgb(117, 108, 198);
    }
</style>
