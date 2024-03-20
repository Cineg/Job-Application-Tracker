import { FadeLoader } from "react-spinners";

function Spinner() {
	return (
		<>
			<FadeLoader
				color="#8fc4d9"
				height={30}
				radius={10}
				width={20}
				margin={40}
			/>
		</>
	);
}

export default Spinner;
