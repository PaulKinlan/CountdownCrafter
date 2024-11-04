function initTimer(timerId) {
    function updateTimer(endDate) {
        const now = new Date().getTime();
        const distance = new Date(endDate).getTime() - now;

        if (distance < 0) {
            document.getElementById('countdown').innerHTML = "Event has ended!";
            return;
        }

        const months = Math.floor(distance / (1000 * 60 * 60 * 24 * 30));
        const days = Math.floor((distance % (1000 * 60 * 60 * 24 * 30)) / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        let display = '';
        if (months > 0) display += `${months}M `;
        if (days > 0) display += `${days}d `;
        display += `${hours}h ${minutes}m ${seconds}s`;

        document.getElementById('countdown').innerHTML = display;
    }

    async function fetchTimerData() {
        const response = await fetch(`/api/timer/${timerId}`);
        const data = await response.json();
        updateTimer(data.end_date);
    }

    // Update immediately and then every second
    fetchTimerData();
    setInterval(fetchTimerData, 1000);
}

function copyToClipboard() {
    const url = window.location.href;
    navigator.clipboard.writeText(url).then(() => {
        alert('Timer URL copied to clipboard!');
    });
}
