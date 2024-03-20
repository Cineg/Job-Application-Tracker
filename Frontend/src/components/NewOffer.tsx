import { useState } from "react";

type newOfferProps = {
	setErrMessage: React.Dispatch<React.SetStateAction<string>>;
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

const API_BASE: string = import.meta.env.VITE_API_URL;

function NewOffer({ setErrMessage, setIsOfferAdded }: newOfferProps) {
	const [companyName, setCompanyName] = useState<string>("");
	const [offerURL, setOfferURL] = useState<string>("");
	const [positionName, setPositionName] = useState<string>("");

	function getFormData(event: React.ChangeEvent<HTMLFormElement>) {
		event.preventDefault();

		fetch(`${API_BASE}/add-offer`, {
			method: "POST",
			body: JSON.stringify({
				company: companyName,
				title: positionName,
				url: offerURL,
			}),
			headers: {
				"Content-type": "application/json; charset=UTF-8",
			},
		})
			.then((response: Response) => response.json())
			.then((json) => {
				if (json["success"] === false) {
					setErrMessage(json["message"]);
					setIsOfferAdded(false);
				} else {
					setIsOfferAdded(true);
					setErrMessage("");
				}
			});
	}
	return (
		<form className="form" onSubmit={getFormData}>
			<div>
				<input
					placeholder="Provide Company Name"
					name="companyName"
					className="input"
					onChange={(e) => setCompanyName(e.target.value)}
				></input>
				<input
					placeholder="Provide Offer URL"
					name="offerURL"
					className="input"
					onChange={(e) => setOfferURL(e.target.value)}
				></input>
				<input
					placeholder="Provide Position Name"
					name="positionName"
					className="input"
					onChange={(e) => setPositionName(e.target.value)}
				></input>
			</div>
			<button type="submit" className="button">
				Add
			</button>
		</form>
	);
}

export default NewOffer;
