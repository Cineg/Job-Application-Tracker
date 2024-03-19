import { OfferData } from "../App";

const API_BASE = import.meta.env.VITE_API_URL;

export function fetchOffers(
	setter: React.Dispatch<React.SetStateAction<OfferData | never[]>>
) {
	fetch(`${API_BASE}/results`, {
		method: "GET",
	})
		.then((response: Response) => response.json())
		.then((json) => {
			setter(json["Offers"]);
		});
}
