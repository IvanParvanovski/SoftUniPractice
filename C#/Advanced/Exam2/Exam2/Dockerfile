FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Exam2/Exam2.csproj", "Exam2/"]
RUN dotnet restore "Exam2/Exam2.csproj"
COPY . .
WORKDIR "/src/Exam2"
RUN dotnet build "Exam2.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Exam2.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Exam2.dll"]
