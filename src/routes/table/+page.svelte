<script lang="ts">
    import { post_stuff } from "$lib/components/call_fapi";
    import { fetch_table } from "$lib/components/call_fapi";
    import { Tabulator } from "tabulator-tables";
    import { onMount } from "svelte";

    let post_body = JSON.stringify({
        name: "fish",
        description: "This is a test product",
        plu: 1234567890,
    });

    onMount(() => {
        let path, body, target;
        let tabledata = fetch_table(post_body).then((data) => {
            var table = new Tabulator("#demo-table", {
                data: data.rows,
                layout: "fitColumns",
                columns: data.columns,
            });
        });
    });
</script>

<h1>API Call Component Testing</h1>
<div class="something">
    {#await post_stuff(post_body)}
        ...await...
    {:then payload}
        {payload.name}
        {payload.description}
        {payload.plu}
    {/await}
</div>
<div id="demo-table"></div>

<style>
    .something {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
</style>
