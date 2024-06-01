<script>
    async function get_stuff() {
        const target = "http://192.168.1.26:8000/";
        const response = await fetch(target);
        const payload = response.json();
        return payload;
    }
</script>

<h1>API Call Testing</h1>
<div class="something">
    {#await get_stuff()}
        ...
    {:then payload}
        = {payload}
    {/await}
</div>
