<script lang="ts">
	import Header from '$lib/components/List/Header.svelte';
	import Item from '$lib/components/List/Item.svelte';

	let bookmarks: Array<string> = ['', '', ''];
	let tasks: Array<string> = [];
	let notes: Array<string> = [];

	const addBookmark = () => {
		bookmarks = [...bookmarks, ''];
	};
	const addTask = () => {
		tasks = [...tasks, ''];
	};
	const addNote = () => {
		notes = [...notes, ''];
	};
</script>

<div class="container-rows">
	<div class="container-column">
		<Header title="bookmarks" plusClick={addBookmark} />
		<div class="reverse">
			{#each bookmarks as bookmark}
				<Item content={bookmark} />
			{/each}
		</div>
	</div>
	<div class="container-column">
		<Header title="tasks" plusClick={addTask} />
		{#each tasks as task}
			<Item content={task} />
		{/each}
	</div>
	<div class="container-column">
		<Header title="notes" plusClick={addNote} />
		{#each notes as note}
			<Item content={note} />
		{/each}
	</div>
</div>

<style lang="scss">
	.container-rows {
		display: flex;
		justify-content: center;
		flex-direction: row;
		height: 100%;
		gap: 40px;
		margin: 20px 60px 20px 60px;
	}
	.container-column {
		background-color: #555;
		display: flex;
		flex-direction: column;
		width: 100%;
		min-height: 300px;
		gap: 4px;
		border-radius: 0px;
		box-shadow: 10px 20px 40px #0002;
		padding-bottom: 15px;
	}
	.reverse {
		display: flex;
		flex-direction: column-reverse;
		gap: 4px;
	}
</style>
