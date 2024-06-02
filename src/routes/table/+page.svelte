<script>
    import { post_stuff } from "$lib/components/call_fapi";
    import { Tabulator } from "tabulator-tables";
    import { onMount } from "svelte";

    let post_body = JSON.stringify({
        name: "fish",
        description: "This is a test product",
        plu: 1234567890,
    });

    let tabledata = [
        { id: 1, name: "Oli Bob", age: "12", col: "red", dob: "" },
        { id: 2, name: "Mary May", age: "1", col: "blue", dob: "14/05/1982" },
        {
            id: 3,
            name: "Christine Lobowski",
            age: "42",
            col: "green",
            dob: "22/05/1982",
        },
        {
            id: 4,
            name: "Brendon Philips",
            age: "125",
            col: "orange",
            dob: "01/08/1980",
        },
        {
            id: 5,
            name: "Margret Marmajuke",
            age: "16",
            col: "yellow",
            dob: "31/01/1999",
        },
    ];
    let columnsettings = [
        { title: "Name", field: "name", width: 150 },
        {
            title: "Age",
            field: "age",
            align: "left",
            formatter: "progress",
        },
        { title: "Favourite Color", field: "col" },
        {
            title: "Date Of Birth",
            field: "dob",
            sorter: "date",
            align: "center",
        },
    ];

    onMount(() => {
        var table = new Tabulator("#demo-table", {
            data: tabledata,
            layout: "fitColumns",
            columns: columnsettings,
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
