const date_selectors = {
	start_date: document.getElementById('start_date'),
	end_date: document.getElementById('end_date'),
};

function format_date(date) {
	const month = (date.getMonth() + 1).toString().padStart(2, '0');
	const day = date.getDate().toString().padStart(2, '0');
	const year = date.getFullYear();
	return `${year}-${month}-${day}`;
}

function format_time(time_string) {
	const date = new Date(time_string);
	return date.toLocaleString();
}

async function get_stats() {
	const today = new Date();
	const start_date = (() => {
		const value = date_selectors.start_date.value;
		if (value !== '') {
			return value;
		}
		const date = new Date(today.valueOf());
		date.setDate(date.getDate() - 7);
		return format_date(date);
	})();
	const end_date = (() => {
		const value = date_selectors.end_date.value;
		if (value !== '') {
			return value;
		}
		return format_date(today);
	})();

	const response = await fetch(
		`/api/reports/renewalstats/?format=json&start_date=${start_date}&end_date=${end_date}`
	);
	const data = await response.json();

	return data;
}

function update_auto_table(data) {
	const table = document.getElementById('auto_renewal_table');
	const tbody = table.querySelector('tbody');
	tbody.innerHTML = '';
	data.forEach((row) => {
		const tr = document.createElement('tr');
		tr.innerHTML = `
			<td>${row.hostname}</td>
			<td>${row.mac}</td>
			<td>${format_time(row.expires)}</td>
			<td>${format_time(row.changed)}</td>
		`;
		tbody.appendChild(tr);
	});
	if (data.length === 0) {
		const tr = document.createElement('tr');
		tr.innerHTML =
			'<td colspan="4">No hosts were automatically renewed in the specified timeframe.</td>';
		tbody.appendChild(tr);
	}
}

function update_manual_table(data) {
	const table = document.getElementById('manual_renewal_table');
	const tbody = table.querySelector('tbody');
	tbody.innerHTML = '';
	data.forEach((row) => {
		const last_seen = (() => {
			console.log(row.last_seen == null);
			if (row.last_seen == null) {
				return '<span class="text-danger">No data</span>';
			}
			return format_time(row.last_seen);
		})();
		const tr = document.createElement('tr');
		if (row.last_seen == null) {
			tr.classList.add('table-danger');
		}
		const hostname_td = document.createElement('td');
		hostname_td.textContent = row.hostname;
		const mac_td = document.createElement('td');
		mac_td.textContent = row.mac;
		const expires_td = document.createElement('td');
		expires_td.textContent = format_time(row.expires);
		const changed_td = document.createElement('td');
		changed_td.textContent = format_time(row.changed);
		const last_seen_td = document.createElement('td');
		last_seen_td.innerHTML = last_seen;
		const delete_td = document.createElement('td');
		const delete_button = document.createElement('button');
		delete_button.type = 'button';
		delete_button.classList.add(
			'btn',
			row.last_seen == null ? 'btn-danger' : 'btn-default'
		);
		delete_button.id = `delete-${row.hostname}`;
		// Only allow deletion if device doesn't have last_seen data
		delete_button.disabled = row.last_seen != null;
		delete_button.innerHTML =
			'<span class="glyphicon glyphicon-trash" aria-label="Delete"/>';
		delete_button.addEventListener('click', () => {
			// Confirm deletion
			if (!confirm(`Really delete host ${row.hostname}?`)) {
				return;
			}
			$.ajax({
				url: `/api/hosts/${row.mac}/delete/`,
				type: 'POST',
				success: () => {
					tr.remove();
				},
				error: (jqXHR, textStatus, errorThrown) => {
					alert(
						`Error deleting host ${row.hostname}: ${textStatus} ${errorThrown}`
					);
				},
			});
		});
		delete_td.appendChild(delete_button);
		tr.appendChild(hostname_td);
		tr.appendChild(mac_td);
		tr.appendChild(expires_td);
		tr.appendChild(changed_td);
		tr.appendChild(last_seen_td);
		tr.appendChild(delete_td);
		tbody.appendChild(tr);
		tbody.appendChild(tr);
	});
	if (data.length === 0) {
		const tr = document.createElement('tr');
		tr.innerHTML =
			'<td colspan="6">No soon-to-expire hosts were manually renewed in the specified timeframe.</td>';
		tbody.appendChild(tr);
	}
}

function update_unrenewed_table(data) {
	const table = document.getElementById('unrenewed_table');
	const tbody = table.querySelector('tbody');
	tbody.innerHTML = '';
	data.forEach((row) => {
		const last_seen = (() => {
			if (row.last_seen == null) {
				return '<span class="text-danger">No data</span>';
			}
			return format_time(row.last_seen);
		})();
		const tr = document.createElement('tr');
		const hostname_td = document.createElement('td');
		hostname_td.textContent = row.hostname;
		const mac_td = document.createElement('td');
		mac_td.textContent = row.mac;
		const expires_td = document.createElement('td');
		expires_td.textContent = format_time(row.expires);
		const last_notified_td = document.createElement('td');
		last_notified_td.textContent = format_time(row.last_notified);
		const last_seen_td = document.createElement('td');
		last_seen_td.innerHTML = last_seen;
		const renew_td = document.createElement('td');
		const renew_button = document.createElement('button');
		renew_button.type = 'button';
		renew_button.classList.add('btn', 'btn-primary');
		renew_button.id = `renew-${row.hostname}`;
		renew_button.innerHTML =
			'<span class="glyphicon glyphicon-refresh" aria-label="Renew"/>';
		renew_button.addEventListener('click', () => {
			if (
				row.last_seen == null &&
				!confirm(
					`Host ${row.hostname} hasn't been seen in a while. Are you sure you want to renew it?`
				)
			) {
				return;
			}
			$.ajax({
				url: `/api/hosts/${row.mac}/renew/`,
				type: 'POST',
				dataType: 'json',
				data: {
					expire_days: '30',
				},
				success: () => {
					tr.remove();
				},
				error: (jqXHR, textStatus, errorThrown) => {
					alert(
						`Error renewing host ${row.hostname}: ${textStatus} ${errorThrown}`
					);
				},
			});
		});
		renew_td.appendChild(renew_button);
		tr.appendChild(hostname_td);
		tr.appendChild(mac_td);
		tr.appendChild(expires_td);
		tr.appendChild(last_notified_td);
		tr.appendChild(last_seen_td);
		tr.appendChild(renew_td);
		tbody.appendChild(tr);
	});
	if (data.length === 0) {
		const tr = document.createElement('tr');
		tr.innerHTML =
			'<td colspan="6">No unrenewed hosts had notifications sent in the specified timeframe.</td>';
		tbody.appendChild(tr);
	}
}

function update_summary_table(data) {
	const auto_count_el = document.getElementById('auto_count');
	const manual_count_el = document.getElementById('manual_count');
	const unrenewed_count_el = document.getElementById('unrenewed_count');

	auto_count_el.textContent = data.auto_renewed.length;
	manual_count_el.textContent = data.notified_renewed.length;
	unrenewed_count_el.textContent = data.notified_unrenewed.length;
}

async function update_tables() {
	const stats = await get_stats();

	update_summary_table(stats);

	update_auto_table(stats.auto_renewed);
	update_manual_table(stats.notified_renewed);
	update_unrenewed_table(stats.notified_unrenewed);
}

function init() {
	const today = new Date();
	date_selectors.start_date.value = format_date(
		new Date(today.valueOf() - 7 * 24 * 60 * 60 * 1000)
	);
	date_selectors.end_date.value = format_date(today);
	document
		.getElementById('update_button')
		.addEventListener('click', update_tables);

	update_tables();
}

init();
