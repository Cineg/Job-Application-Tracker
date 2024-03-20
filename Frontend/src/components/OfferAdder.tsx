import { useState } from "react";
import "./OfferAdder.css";

const API_BASE: string = import.meta.env.VITE_API_URL;

type offerAdderProp = {
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

type newOfferProps = {
	setErrMessage: React.Dispatch<React.SetStateAction<string>>;
	setIsOfferAdded: React.Dispatch<React.SetStateAction<boolean>>;
};

function OfferAdder({ setIsOfferAdded }: offerAdderProp) {
	const [errMessage, setErrMessage] = useState<string>("");

	return (
		<div className="wrapper">
			<p>
				Oops! Looks like there are no matches for this offer. Care to
				add one?
			</p>
			<NewOffer
				setErrMessage={setErrMessage}
				setIsOfferAdded={setIsOfferAdded}
			></NewOffer>
			{errMessage === "" ? (
				<></>
			) : (
				<p className="err-message">{errMessage}</p>
			)}
		</div>
	);
}

function NewOffer({ setErrMessage, setIsOfferAdded }: newOfferProps) {
	function getFormData(event: React.ChangeEvent<HTMLFormElement>) {
		event.preventDefault();

		const formData = new FormData(event.target);
		const companyName = formData.get("companyName");
		const offerURL = formData.get("offerURL");
		const positionName = formData.get("positionName");

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
				></input>
				<input
					placeholder="Provide Offer URL"
					name="offerURL"
					className="input"
				></input>
				<input
					placeholder="Provide Position Name"
					name="positionName"
					className="input"
				></input>
			</div>
			<button type="submit" className="button">
				Add
			</button>
		</form>
	);
}

export default OfferAdder;
