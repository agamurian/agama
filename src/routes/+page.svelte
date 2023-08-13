<script lang="ts">
	import Settings from '$lib/components/Settings.svelte';
	import Player from '$lib/components/Player.svelte';
	import BottomSqaures from './(components)/BottomSqaures.svelte';
	import SearchInternet from './(components)/SearchInternet.svelte';

	let time = new Date();
	function setTime() {
		time = new Date();
	}
	setInterval(setTime, 1000);
	function formatToHM(time: Date) {
		return time.toLocaleTimeString('en-US', {
			hour12: false,
			hour: 'numeric',
			minute: 'numeric'
		});
	}
	function formatToDay(time: Date) {
		const theDay = time.toLocaleDateString('pt-PT').replaceAll('/', '.');
		return theDay;
	}
	$: HM = formatToHM(time);
	$: day = formatToDay(time);
</script>

<div class="container">
	<p class="hm f-sans f-800">
		{HM}
	</p>
	<p class="day f-sans f-500 f-22">
		{day}
	</p>

	<br />
	<div class="container-center">
		<SearchInternet />
	</div>

	<br />
	<BottomSqaures />
	<Settings />
	<Player />
</div>

<style lang="scss">
	.container {
		max-width: 1600px;
		padding: 20px;
		gap: 40px;
	}
	.container-center {
		display: flex;
		justify-content: center;
		margin: 0;
		flex-direction: row;
	}
	.hm {
		margin: 0px;
		font-size: 120px;
		text-align: center;
	}
	.day {
		margin: 0px;
		text-align: center;
	}
</style>
