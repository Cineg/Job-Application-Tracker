import "./JobModal.css";

type ModalProp = {
	children: React.ReactNode;
};

function Modal({ children }: ModalProp) {
	return <div className="container"> {children}</div>;
}

export default Modal;
