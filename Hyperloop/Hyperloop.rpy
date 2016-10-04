I-Logix-RPY-Archive version 8.12.0 C++ 9728113
{ IProject 
	- _id = GUID 9bb40740-b985-48f4-b961-57c04b9633e2;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 1;
			- value = 
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowPredefinedPackage";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
				}
			}
		}
	}
	- _name = "Hyperloop";
	- Stereotypes = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IHandle 
			- _m2Class = "IStereotype";
			- _filename = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy\\SysML.sbs";
			- _subsystem = "SysML";
			- _class = "";
			- _name = "SysML";
			- _id = GUID 052b8171-a32b-4f45-a829-5585f79f9deb;
		}
	}
	- _modifiedTimeWeak = 10.2.2016::17:39:59;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "ActorPkg.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "ActorPkg";
		- _id = GUID 5a8e315d-60e3-44be-9b7a-5222dfe4b9e8;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 0b64f8fa-1dfb-407c-b5ea-320c72f3f2e5;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 8;
		- value = 
		{ IProfile 
			- fileName = "SysML";
			- _persistAs = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy";
			- _id = GUID d9689b73-885e-44c4-896b-de43defa0a33;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "HarmonySE";
			- _persistAs = "$OMROOT\\Profiles\\HarmonySE";
			- _id = GUID 29d4fccc-40d9-4cb3-af8a-d7464f198819;
			- _isReference = 1;
		}
		{ ISubsystem 
			- fileName = "ActorPkg";
			- _id = GUID 5a8e315d-60e3-44be-9b7a-5222dfe4b9e8;
		}
		{ ISubsystem 
			- fileName = "DesignSynthesisPkg";
			- _id = GUID 8ec05481-631f-4d72-b378-6279922c81a7;
		}
		{ ISubsystem 
			- fileName = "FunctionalAnalysisPkg";
			- _id = GUID 8f77d0f5-4334-4f9a-939b-d76840516788;
		}
		{ ISubsystem 
			- fileName = "InterfacesPkg";
			- _id = GUID 7d37ece1-54e7-4dac-a533-8f23f4168795;
		}
		{ ISubsystem 
			- fileName = "TypesPkg";
			- _id = GUID a2c926ac-d26f-4f33-9f1a-bdb1488501b0;
		}
		{ ISubsystem 
			- fileName = "RequirementsAnalysisPkg";
			- _id = GUID 299f5927-1259-4102-8647-4a76099799d7;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 0b64f8fa-1dfb-407c-b5ea-320c72f3f2e5;
		}
	}
}

