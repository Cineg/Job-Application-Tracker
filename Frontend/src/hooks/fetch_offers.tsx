import { Offer } from "../App";

const API_BASE = import.meta.env.VITE_API_URL;

export async function fetchOffers(): Promise<Offer[] | never[]> {
	try {
		const response = await fetch(`${API_BASE}/results`, {
			method: "GET",
		});

		if (!response.ok) {
			throw new Error(`Failed to fetch data: ${response.statusText}`);
		}

		const data = await response.json();
		return data["Offers"];
	} catch (error) {
		console.error("Error fetching data:", error);
		return [];
	}
}
