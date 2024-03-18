import React from "react";

function OfferAdder() {
	const formStyle: React.CSSProperties = {
		padding: "1rem",
		display: "flex",
		flexDirection: "column",
		placeItems: "center",
	};

	const inputStyle: React.CSSProperties = {
		padding: ".5rem",
		margin: "0 .5rem",
		borderRadius: "5px",
		border: "1px solid transparent",
	};

	const buttonStyle: React.CSSProperties = {
		width: "10rem",
		marginTop: "1rem",
	};

	function getFormData(event: Event) {
		event.preventDefault();

		const formData = new FormData(event.target);
		const companyName = formData.get("companyName");
		const offerURL = formData.get("offerURL");
		const positionName = formData.get("positionName");

		console.log(companyName, offerURL, positionName);
	}

	return (
		<>
			<form style={formStyle} onSubmit={getFormData}>
				<div>
					<input
						placeholder="Provide Company Name"
						name="companyName"
						style={inputStyle}
					></input>
					<input
						placeholder="Provide Offer URL"
						name="offerURL"
						style={inputStyle}
					></input>
					<input
						placeholder="Provide Position Name"
						name="positionName"
						style={inputStyle}
					></input>
				</div>
				<button type="submit" style={buttonStyle}>
					Add
				</button>
			</form>
		</>
	);
}

export default OfferAdder;
