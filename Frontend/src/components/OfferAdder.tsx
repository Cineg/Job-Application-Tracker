import "./OfferAdder.css";

function OfferAdder() {
	function getFormData(event: React.ChangeEvent<HTMLFormElement>) {
		event.preventDefault();

		const formData = new FormData(event.target);
		const companyName = formData.get("companyName");
		const offerURL = formData.get("offerURL");
		const positionName = formData.get("positionName");

		console.log(companyName, offerURL, positionName);
	}

	return (
		<>
			<p>
				Oops! Looks like there are no matches for this offer. Care to
				add one?
			</p>
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
		</>
	);
}

export default OfferAdder;
