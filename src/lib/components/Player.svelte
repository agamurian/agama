<script lang="js">
	import Play from './Icons/Play.svelte';
	import Modal from './Modal.svelte';

	let modalOpened = false;
	let play = false;
	let currentTime = '00:00';
	let songs = [
		{
			name: 'Song about me',
			duration: '03:33',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Song about me',
			duration: '02:22',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'about Song me',
			duration: '01:24',
			author: 'Arctic Monkeys',
			active: true,
		},
		{
			name: 'Saboutazh me',
			duration: '33:43',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Stare at me',
			duration: '13:11',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Song about me',
			duration: '03:33',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Song about me',
			duration: '02:22',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'about Song me',
			duration: '01:24',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Saboutazh me',
			duration: '33:43',
			author: 'Arctic Monkeys',
			active: false,
		},
		{
			name: 'Stare at me',
			duration: '13:11',
			author: 'Arctic Monkeys',
			active: false,
		},
	]
</script>

<div
	class="play-button"
	on:click={() => {
		modalOpened = true;
	}}
>
	<Play color="#ccc" size={20} />
</div>

<Modal bind:modalOpened>

	{#each songs as song}

		<div class="option"
				class:active={song.active}
		>

			<div
				class="play-button-player"
				class:active={song.active}
				on:click={() => {
					play = true;
				}}
			>
				<Play color="#ccc" size={20} />
			</div>
			<div class="track">
				{song.name}
			</div>
			<div class="author">
				{song.author}
			</div>
			<div class="time">
				{currentTime}/{song.duration}
			</div>

		</div>

	{/each}


</Modal>

<style lang="css">
	.option {
		font-size: 15px;
		padding: 15px 15px;
		gap: 2px;
		background-color: dimgray;
		display: flex;
		flex-direction: row;
		color: #dddd;
		background-color: #301014;
		border-bottom: 2px dotted #4444;
	}
	.play-button {
		position: fixed;
		border-radius: 10px;
		height: 40px;
		width: 40px;
		top: 20px;
		left: 20px;
		background-color: #444;
		display: flex;
		justify-content: center;
		cursor: pointer;
		&:hover {
			background-color: #8a3434;
		}
	}
	.play-button-player {
		position: relative;
		display: flex;
		border-radius: 10px;
		height: 40px;
		width: 40px;
		background-color: #4237;
		display: flex;
		justify-content: center;
		cursor: pointer;
		border: 1px solid #7772;
		&:hover {
			background-color: #8a3454;
		}
	}
	.track{
		display: flex;
		flex: 1;
		padding: 10px;
		font-weight: 500;
	}
	.author{
		display: flex;
		flex: 1;
		padding: 15px;
		font-weight: 300;
		font-size: 10px;
	}
	.time{
		display: flex;
		flex: 0;
		padding: 10px;
		font-weight: 300;
	}
	.active {
		background-color: #4354;
		color: antiquewhite;
	}
</style>
